from base64 import b64encode

def to_dict(p):
    return {
        "id": p.id,
        "filename": p.filename,
        "label": p.label,
        "confidence": p.confidence,
        "woundImage": b64encode(p.woundImage).decode("utf-8") if p.woundImage else None,
    }