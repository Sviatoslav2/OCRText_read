import argparse

from paddleocr import PaddleOCR

ocr = PaddleOCR(rec_model_dir='/opt/program/pretrain/en_PP-OCRv3_rec_infer/',
                det_model_dir='/opt/program/pretrain/en_PP-OCRv3_det_infer/',
                cls_model_dir='/opt/program/pretrain/ch_ppocr_mobile_v2.0_cls_infer/',
                use_angle_cls=True, lang='en')


def extract_paddle_result(img_path: str) -> list:
    """
    :param img_path: str
    :return: [[box, [txt, score]], ...]
    """
    result = ocr.ocr(img_path, rec=True, det=True, cls=True)
    return result


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--image", type=str, default="tmp.png")
    args = args.parse_args()

    input_f = args.image
    print(extract_paddle_result(input_f))
