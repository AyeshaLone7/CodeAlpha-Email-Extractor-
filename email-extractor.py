import re      # to find email pattern 
import os      # to check if file exist or not
import shutil  #to make copy in backup

print("=" * 40)
print("       EMAIL EXTRACTOR")
print("=" * 40)

input_file = input("\nEnter File name from which you want to extract emails? (e.g. data.txt): ").strip()

if not os.path.exists(input_file):
    print(f"\n\n✘ '{input_file}' not found!")
    print("  Put file in same folder and run again.")
    exit()
with open(input_file, "r") as f:
    content = f.read()   

print(f"\n✔Read the file: {input_file}")

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
all_emails = re.findall(pattern, content)
unique_emails = sorted(set(all_emails))

total_found  = len(all_emails)
total_unique = len(unique_emails)
duplicates   = total_found - total_unique

print("\n" + "=" * 40)
print("        EXTRACTION REPORT")
print("=" * 40)
print(f"Total emails found   : {total_found}")
print(f"Unique emails        : {total_unique}")
print(f"Duplicates removed   : {duplicates}")
print("-" * 40)
print("UNIQUE EMAILS:")
print("-" * 40)
for i, email in enumerate(unique_emails, start=1):
    print(f"  {i}. {email}")
print("=" * 40)

output_file = input("\nIn which file you want to emails? (e.g. results.txt): ").strip()

with open(output_file, "w") as f:
    f.write("EMAIL EXTRACTION REPORT\n")
    f.write("=" * 40 + "\n")
    f.write(f"Source File      : {input_file}\n")
    f.write(f"Total Found      : {total_found}\n")
    f.write(f"Unique Emails    : {total_unique}\n")
    f.write(f"Duplicates       : {duplicates}\n")
    f.write("-" * 40 + "\n")
    for i, email in enumerate(unique_emails, start=1):
        f.write(f"  {i}. {email}\n")
    f.write("=" * 40 + "\n")

print(f"  ✔ Saved to      : {output_file}")

backup_file = "backup_" + output_file
shutil.copy(output_file, backup_file)
print(f"  ✔ Backup saved  : {backup_file}")

print("\n[Program finished]")
  
