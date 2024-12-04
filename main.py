import requests
import os
from PyPDF2 import PdfMerger

chapters_intro = ["preface.pdf", "toc.pdf", "dialogue-threeeasy.pdf", "intro.pdf"]
chapters_virtulization = [
    "dialogue-virtualization.pdf",
    "cpu-intro.pdf",
    "cpu-api.pdf",
    "cpu-mechanisms.pdf",
    "cpu-sched.pdf",
    "cpu-sched-mlfq.pdf",
    "cpu-sched-lottery.pdf",
    "cpu-sched-multi.pdf",
    "cpu-dialogue.pdf",
    "dialogue-vm.pdf",
    "vm-intro.pdf",
    "vm-api.pdf",
    "vm-mechanism.pdf",
    "vm-segmentation.pdf",
    "vm-freespace.pdf",
    "vm-paging.pdf",
    "vm-tlbs.pdf",
    "vm-smalltables.pdf",
    "vm-beyondphys.pdf",
    "vm-beyondphys-policy.pdf",
    "vm-complete.pdf",
    "vm-dialogue.pdf",
]
chapters_concurrency = [
    "dialogue-concurrency.pdf",
    "threads-intro.pdf",
    "threads-api.pdf",
    "threads-locks.pdf",
    "threads-locks-usage.pdf",
    "threads-cv.pdf",
    "threads-sema.pdf",
    "threads-bugs.pdf",
    "threads-events.pdf",
    "threads-dialogue.pdf",
]
chapters_peristence = [
    "dialogue-persistence.pdf",
    "file-devices.pdf",
    "file-disks.pdf",
    "file-raid.pdf",
    "file-intro.pdf",
    "file-implementation.pdf",
    "file-ffs.pdf",
    "file-journaling.pdf",
    "file-lfs.pdf",
    "file-ssd.pdf",
    "file-integrity.pdf",
    "file-dialogue.pdf",
    "dialogue-distribution.pdf",
    "dist-intro.pdf",
    "dist-nfs.pdf",
    "dist-afs.pdf",
    "dist-dialogue.pdf",
]
chapters_security = [
    "dialogue-security.pdf",
    "security-intro.pdf",
    "security-authentication.pdf",
    "security-access.pdf",
    "security-crypto.pdf",
    "security-distributed.pdf",
]
appendices = [
    "dialogue-vmm.pdf",
    "vmm-intro.pdf",
    "dialogue-monitors.pdf",
    "threads-monitors.pdf",
    "dialogue-labs.pdf",
    "lab-tutorial.pdf",
    "lab-projects-systems.pdf",
    "lab-projects-xv6.pdf",
]


def download_file(url, save_path):
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"File saved to {save_path}")
    else:
        print(
            f"Failed to download file. Status code: {response.status_code}, url: {url}"
        )
        raise Exception


def merge_pdf(pdf_paths, output_file_name):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Add all PDFs to the merger
    for pdf in pdf_paths:
        merger.append(pdf)

    # Write the merged PDF to a file
    merger.write(output_file_name)
    merger.close()


def main():
    save_dir = "./pdfs/"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    base_url = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
    chapters = [
        chapters_intro,
        chapters_virtulization,
        chapters_concurrency,
        chapters_peristence,
        chapters_security,
        appendices,
    ]
    pdf_paths = []
    for chapter in chapters:
        for section in chapter:
            p = "./pdfs/" + section
            pdf_paths.append(p)
            if os.path.exists(p):
                continue
            download_file(base_url + section, p)

    merge_pdf(pdf_paths, "ostep.pdf")


if __name__ == "__main__":
    main()
