FROM paddlepaddle/paddle:2.4.0

RUN mkdir -p /app
COPY . /app
WORKDIR /app

ENV LANG=en_US.utf8
ENV LANG=C.UTF-8

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install paddleocr==2.6.1.1

RUN git clone -b release/2.6 https://github.com/PaddlePaddle/PaddleOCR.git /opt/program/
RUN mkdir /opt/program/pretrain/

RUN wget -P /opt/program/pretrain/ https://paddleocr.bj.bcebos.com/PP-OCRv3/english/en_PP-OCRv3_det_infer.tar && tar -xf /opt/program/pretrain/en_PP-OCRv3_det_infer.tar -C /opt/program/pretrain/ && rm -rf /opt/program/pretrain/en_PP-OCRv3_det_infer.tar
RUN wget -P /opt/program/pretrain/ https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar && tar -xf /opt/program/pretrain/ch_ppocr_mobile_v2.0_cls_infer.tar -C /opt/program/pretrain/ && rm -rf /opt/program/pretrain/ch_ppocr_mobile_v2.0_cls_infer.tar
RUN wget -P /opt/program/pretrain/ https://paddleocr.bj.bcebos.com/PP-OCRv3/english/en_PP-OCRv3_rec_infer.tar && tar -xf /opt/program/pretrain/en_PP-OCRv3_rec_infer.tar -C /opt/program/pretrain/ && rm -rf /opt/program/pretrain/en_PP-OCRv3_rec_infer.tar


EXPOSE 80

CMD ["bash", "run.sh"]