import re


def parse_mtype_descr(desc):
    """
    Parse Machine Type description and return vCPU number and RAM in GB
    :param desc: Raw description value from GCP API
    :return: {vcpu_num, ram_gb}
    """
    # print(f'start: parse_mtype_descr("{desc}")')
    re_cpu = re.search("\w+ vCPU", desc)
    vcpu_num = str(re_cpu[0]).split(" ")[0]
    re_ram = re.search("[\w.]+ \w+ RAM", desc)
    ram_gb = str(re_ram[0]).split(" ")[0]
    ram_unit = str(re_ram[0]).split(" ")[1]
    # print(f'ram:{ram_gb}  unit:{ram_unit}')
    if ram_unit == 'TB':
        ram_gb = float(ram_gb)*1024
    return vcpu_num, ram_gb


descs = []

descs.append("Compute Optimized: 16 vCPUs, 64 GB RAM")
descs.append('Compute Optimized: 96 vCPUs, 624 GB RAM')
descs.append('Compute Optimized: 96 vCPUs, 1.4 TB RAM')
descs.append('Compute Optimized: 1 vCPU, 3.75 GB RAM')
descs.append('Compute Optimized: 16 vCPUs, 60 GB RAM')
descs.append('Compute Optimized: 16 vCPUs, 64 GB RAM')

for desc in descs:
    print(desc)
    print(f' - {parse_mtype_descr(desc)}')