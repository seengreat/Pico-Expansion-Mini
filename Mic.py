import board
import analogio
import busio
from time import sleep
# 配置 ADC 和 UART
adc_pin = analogio.AnalogIn(board.A2)  
uart = busio.UART(board.GP0, board.GP1, baudrate=115200)  # UART 配置 (TX=GP0, RX=GP1)

def get_adc_value():
    adc = adc_pin.value  # 读取 ADC 原始值（范围 0-65535）
    adc_str = f"adc: {adc}\r\n"
    uart.write(adc_str.encode('utf-8'))  # 通过 UART 发送
    print(adc_str)  # 打印 ADC 值到终端

def get_volt_value():
    adc = adc_pin.value  # 读取 ADC 原始值（范围 0-65535）
    volt = (adc * 3.3) / 65535
    volt_str = f"volt: {volt:.2f}V\r\n"
    uart.write(volt_str.encode('utf-8'))  # 通过 UART 发送
    print(volt_str)  # 打印电压值到终端

# 主循环
if __name__ == '__main__':
    while True:
        get_volt_value()
        sleep(0.05)  # 延时 50ms
