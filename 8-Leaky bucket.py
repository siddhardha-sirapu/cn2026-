def leaky_bucket():
    bucket_size = int(input("Enter bucket size: "))
    outgoing_rate = int(input("Enter outgoing rate: "))
    num_inputs = int(input("Enter number of inputs: "))
    store = 0
    while num_inputs > 0:
        incoming = int(input("\nEnter the incoming packet size: "))
        print(f"Incoming packet size: {incoming}")
        if incoming <= (bucket_size - store):
            store += incoming
            print(f"Bucket buffer size: {store} out of {bucket_size}")
        else:
            dropped = incoming - (bucket_size - store)
            print(f"Dropped {dropped} packets.")
            store = bucket_size
            print(f"Bucket buffer size: {store} out of {bucket_size}")
        if store >= outgoing_rate:
            store -= outgoing_rate
        else:
            store = 0
        print(f"After outgoing, {store} packets left in buffer out of {bucket_size}")
        num_inputs -= 1

if __name__ == "__main__":
    leaky_bucket()
