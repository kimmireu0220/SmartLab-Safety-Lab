# SmartLab-Safety-Lab

SmartLab 실험실 안전 상태 모니터링 정적 데모 프로젝트입니다.

## Deploy (GitHub Pages)

이 프로젝트는 정적 데모 페이지(`index.html`)로 동작하며, GitHub Pages에 바로 배포할 수 있습니다.
Flask 서버 없이 링크로 바로 시연 가능합니다.

1. GitHub 저장소 -> `Settings` -> `Pages`
2. Source를 `GitHub Actions`로 선택
3. `main` 브랜치에 푸시
4. Actions의 `Deploy Static Site to GitHub Pages` 워크플로우 완료 확인

배포 URL 예시: `https://kimmireu0220.github.io/SmartLab-Safety-Lab/`

## GitHub Actions 자동 배포

`main` 브랜치에 푸시할 때마다 GitHub Pages 자동 배포가 실행됩니다.

워크플로우 파일: `.github/workflows/deploy-render.yml`

정적 자산 빌드 결과물은 `dist/`에 생성되어 Pages에 배포됩니다.
