FROM ubuntu:latest

RUN apt-get update && apt-get dist-upgrade && apt -y install qemu-system-x86
RUN apt-get install cpio socat python3 python3-pip -yyq

RUN pip3 install requests

RUN mkdir -p /task/fs
RUN mkdir -p /task/kernel

COPY bzImage /task/kernel/
COPY compr.sh  decompress.sh initramfs.cpio.gz  run.sh /task/fs/
COPY deploy_manager.py /
RUN chmod ugo+rx /deploy_manager.py && chmod ugo-w /deploy_manager.py
RUN chmod ugo+rx /task/fs/run.sh && chmod ugo-w /task/fs/run.sh
RUN chmod ugo+rx /task/fs/decompress.sh && chmod ugo-w /task/fs/decompress.sh
RUN chmod ugo+rx /task/fs/compr.sh && chmod ugo-w /task/fs/compr.sh
RUN chmod ugo+rx /task/fs/initramfs.cpio.gz && chmod ugo-w /task/fs/initramfs.cpio.gz
RUN chmod ugo+rx /task/kernel/bzImage && chmod ugo-w /task/kernel/bzImage

ENV  PYTHONUNBUFFERED true

WORKDIR /

CMD ["socat", "TCP-LISTEN:9000,reuseaddr,fork,keepalive", "EXEC:./deploy_manager.py"]
