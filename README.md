# SmartLab-Safety-Lab

SmartLab 실험실 안전 상태 대시보드(Flask) 프로젝트입니다.

## Local Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Deploy (Render)

1. [Render](https://render.com) 가입/로그인
2. `New +` -> `Web Service`
3. GitHub 저장소 `kimmireu0220/SmartLab-Safety-Lab` 연결
4. 설정값 입력
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. `Create Web Service` 클릭

배포 완료 후 발급되는 URL(예: `https://smartlab-safety-lab.onrender.com`)로 외부에서 접속 가능합니다.
