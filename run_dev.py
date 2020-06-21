import os

if __name__ == "__main__":
    print("개발용입니다. production 사용 시 SECRET_KEY를 설정해주세요")

    os.environ["FLASK_SECRET_KEY"] = "dev"
    os.environ["JWT_SECRET_KEY"] = "dev"
    os.environ["FLASK_ENV"] = "dev"

    from amuapi import app

    app.run(debug=True, host="0.0.0.0", port=4000)

