import os
import sys
import time
import requests

#remember anaconda
cmd = 'CUDA_VISIBLE_DEVICES=%d'  #order
text = "Already get GPU: %d"  #IFTTT text
memory_value = 100  #triggle value


#IFTTT send message
def send_notice(event_name, key, text):
    url = "https://maker.ifttt.com/trigger/"+event_name+"/with/key/"+key+""
    payload = "{\n    \"value1\": \""+text+"\"\n}"
    headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
    'Host': "maker.ifttt.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "63",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)

#get gpu information
def gpu0_info(gpu_index=0):  #gpu0
    info = os.popen('nvidia-smi|grep %').read().split('\n')[gpu_index].split('|')
    power = int(info[1].split()[-3][:-1])
    memory = int(info[2].split('/')[0].strip()[:-3])
    return power, memory

def gpu1_info(gpu_index=1):  #gpu1
    info = os.popen('nvidia-smi|grep %').read().split('\n')[gpu_index].split('|')
    power = int(info[1].split()[-3][:-1])
    memory = int(info[2].split('/')[0].strip()[:-3])
    return power, memory

def gpu2_info(gpu_index=1):  #gpu2
    info = os.popen('nvidia-smi|grep %').read().split('\n')[gpu_index].split('|')
    power = int(info[1].split()[-3][:-1])
    memory = int(info[2].split('/')[0].strip()[:-3])
    return power, memory

def gpu3_info(gpu_index=1):  #gpu3
    info = os.popen('nvidia-smi|grep %').read().split('\n')[gpu_index].split('|')
    power = int(info[1].split()[-3][:-1])
    memory = int(info[2].split('/')[0].strip()[:-3])
    return power, memory

#scan and get free gpu
def narrow_setup(interval=1):
    gpu_power0, gpu_memory0 = gpu0_info()
    gpu_power1, gpu_memory1 = gpu1_info()
    gpu_power2, gpu_memory2 = gpu2_info()
    gpu_power3, gpu_memory3 = gpu3_info()
    i = 0
    while gpu_memory0 > memory_value and gpu_memory1 > memory_value and gpu_memory2 > memory_value and gpu_memory3 > memory_value:  # set waiting condition
        gpu_power0, gpu_memory0 = gpu0_info()
        gpu_power1, gpu_memory1 = gpu1_info()
        gpu_power2, gpu_memory2 = gpu2_info()
        gpu_power3, gpu_memory3 = gpu3_info()

        i = i % 5
        gpu_power_str0 = 'gpu0 power:%d W |' % gpu_power0
        gpu_memory_str0 = 'gpu0 memory:%d MiB |' % gpu_memory0
        sys.stdout.write('\n' + gpu_memory_str0 + ' ' + gpu_power_str0)

        gpu_power_str1 = 'gpu1 power:%d W |' % gpu_power1
        gpu_memory_str1 = 'gpu1 memory:%d MiB |' % gpu_memory1
        sys.stdout.write('\n' + gpu_memory_str1 + ' ' + gpu_power_str1)

        gpu_power_str2 = 'gpu2 power:%d W |' % gpu_power2
        gpu_memory_str2 = 'gpu2 memory:%d MiB |' % gpu_memory2
        sys.stdout.write('\n' + gpu_memory_str2 + ' ' + gpu_power_str2)

        gpu_power_str3 = 'gpu3 power:%d W |' % gpu_power3
        gpu_memory_str3 = 'gpu3 memory:%d MiB |' % gpu_memory3
        sys.stdout.write('\n' + gpu_memory_str3 + ' ' + gpu_power_str3)
        sys.stdout.write('\n' +'-----------------------------------------------')
        sys.stdout.flush()
        time.sleep(interval)
        i += 1

    if(gpu_memory0 <= memory_value):
        send_notice('GET_GPU', 'czRpb4CrlWCNHMPpq6wWDj', text %(0))
        print('\n' + cmd)
        #os.system(cmd %(0))
    return
    if(gpu_memory1 <= memory_value):
        send_notice('GET_GPU', 'czRpb4CrlWCNHMPpq6wWDj', text %(1))
        print('\n' + cmd)
    	#os.system(cmd %(1))
    return
    if(gpu_memory2 <= memory_value):
        send_notice('GET_GPU', 'czRpb4CrlWCNHMPpq6wWDj', text %(2))
        print('\n' + cmd)
    	#os.system(cmd %(2))
    return
    if(gpu_memory3 <= memory_value):
        send_notice('GET_GPU', 'czRpb4CrlWCNHMPpq6wWDj', text %(3))
        print('\n' + cmd)
    	#os.system(cmd %(3))
    return


if __name__ == '__main__':
    narrow_setup()
