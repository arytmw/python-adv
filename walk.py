import os
import time

parent_path = input("Enter parent path to search: ")

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)

    for child in childs:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            local_time = time.ctime(last_access)
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tLast Access: {local_time}")
            print(f"\tActual Time: {last_access}")
            print(f"\tSize: {size} Bytes")
        elif os.path.isdir(child_path):
            walk_path(child_path)

walk_path(parent_path)
