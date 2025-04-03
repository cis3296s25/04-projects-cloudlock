import time
start_time = time.time()
end_time = time.time()

def generate_aes_key():
    ...

def aes_encrypt(data, key):
    global start_time, end_time
    start_time = time.time()
    ...
    end_time = time.time()

def aes_decrypt(encrypted_data, key):
    global start_time, end_time
    start_time = time.time()
    ...
    end_time = time.time()

def aes_time():
    total_time = end_time - start_time

    return int(total_time)