FROM runpod/pytorch:2.2.1-py3.10-cuda12.1.1-devel-ubuntu22.04
WORKDIR /content
# ENV PATH="/home/camenduru/.local/bin:${PATH}"

# RUN adduser --disabled-password --gecos '' camenduru && \
#     adduser camenduru sudo && \
#     echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
#     chown -R camenduru:camenduru /content && \
#     chmod -R 777 /content && \
#     chown -R camenduru:camenduru /home && \
#     chmod -R 777 /home && \
#     apt update -y && add-apt-repository -y ppa:git-core/ppa && apt update -y && apt install -y aria2 git git-lfs unzip ffmpeg
#
# USER camenduru
# COPY . /content
# WORKDIR /content
COPY . .

RUN pip install -r requirements.txt

# RUN python install.py --default-timeout=100
RUN python run_vidtome.py --default-timeout=100
# RUN pip install -q numba
CMD python run_vidtome.py