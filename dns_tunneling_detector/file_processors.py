import glob
import os


def get_pcaps(directory, ignore_parsed=True):
    all_files = glob.glob(os.path.join(directory, "*.pcap*"))
    parsed_files = glob.glob(os.path.join(directory, "*_parsed.pcap*"))

    if ignore_parsed:
        return list(set(all_files) - set(parsed_files))
    else:
        return all_files


def get_temp_csv(directory):
    return glob.glob(os.path.join(directory, "temp*.csv"))


def concat_csv(csv_path, temp_csv_directory):
    with open(csv_path, "a") as res_csv:
        for temp_csv in get_temp_csv(temp_csv_directory):
            with open(temp_csv) as temp_file:
                for line in temp_file:
                    res_csv.write(line)


def delete_temp_csv(temp_csv_directory):
    for temp_csv in get_temp_csv(temp_csv_directory):
        os.remove(temp_csv)


def mark_pcap_as_read(pcap_file):
    path, filename = os.path.split(pcap_file)
    filename, ext = filename.rsplit(".", maxsplit=1)
    os.rename(pcap_file, os.path.join(path, filename + "_parsed." + ext))
