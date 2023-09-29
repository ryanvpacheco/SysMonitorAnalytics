import psutil
import time
from tabulate import tabulate

def get_process_info():
    processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']))
    process_info = []
    for process in processes:
        pid = process.info['pid']
        name = process.info['name']
        cpu_percent = process.info['cpu_percent']
        memory_info = process.info['memory_info'].rss / (1024 ** 2)  # Convert to MB
        process_info.append((pid, name, cpu_percent, memory_info, time.time()))
    return process_info

def calculate_consumption(data, start_time, end_time):
    cpu_total = 0
    memory_total = 0

    for entry in data:
        if start_time <= entry[4] <= end_time:
            cpu_total += entry[2]
            memory_total += entry[3]

    return cpu_total, memory_total

def save_to_txt(data, total_duration_minutes):
    start_time = data[0][4]
    end_time = start_time + (total_duration_minutes * 60)

    cpu_total, memory_total = calculate_consumption(data, start_time, end_time)

    with open('monitoring_results.txt', 'w') as file:
        table = tabulate(data, headers=["Process ID", "Process Name", "CPU (%)", "Memory (MB)", "Capture Time"])
        file.write(f"{table}\n\n")
        file.write(f"Total CPU Consumido: {cpu_total:.2f}%\n")
        file.write(f"Total Memória Consumida: {memory_total:.2f} MB\n")

def main(total_duration_minutes, interval_seconds=60):
    start_time = time.time()
    end_time = start_time + (total_duration_minutes * 60)

    data = []

    try:
        while time.time() < end_time:
            process_info = get_process_info()
            data.extend(process_info)
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nMonitoramento interrompido manualmente.")

    finally:
        # Salva os dados em um arquivo de texto
        save_to_txt(data, total_duration_minutes)
        print("Resultados salvos em 'monitoring_results.txt'.")

if __name__ == "__main__":
    total_duration_minutes = int(input("Informe a duração total do monitoramento em minutos: "))
    main(total_duration_minutes)
