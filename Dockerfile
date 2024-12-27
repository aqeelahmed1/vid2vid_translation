FROM runpod/pytorch:2.2.1-py3.10-cuda12.1.1-devel-ubuntu22.04
WORKDIR /content
ENV PATH="/home/camenduru/.local/bin:${PATH}"

RUN adduser --disabled-password --gecos '' camenduru && \
    adduser camenduru sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    chown -R camenduru:camenduru /content && \
    chmod -R 777 /content && \
    chown -R camenduru:camenduru /home && \
    chmod -R 777 /home && \
    apt update -y && add-apt-repository -y ppa:git-core/ppa && apt update -y && apt install -y aria2 git git-lfs unzip ffmpeg

USER camenduru

RUN pip install -q clip-interrogator==0.5.4 controlnet-aux==0.0.7 diffusers==0.25.0 open-clip-torch==2.24.0 \
    transformers==4.26.1 accelerate==0.26.1 runpod huggingface_hub==0.25.2
COPY . /content
WORKDIR /content
RUN python install.py --default-timeout=100
RUN python handler.py --default-timeout=100
RUN pip install -q numba
CMD python handler.py