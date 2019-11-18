# jupyterhub

  Use Docker to build a JupyterHub env for mulitiple users to use jupyter notebook.

## 安裝需求
  - docker 
  - docker-compose

## .env & jupyterhub_config.py setting

  ```
  cp env.example .env
  ```
  - `SHARE_FOLDER` 為所有使用者在 container 的 code ，方便未來移植、複製環境
  - port 預設為 `8000` 可依需求更改
  - 新開 port 請更改防火牆設定

  ```
  cp config_folder/example.jupyterhub_config.py config_folder/jupyterhub_config.py
  ```
  - 依需求更改 config 設定

    - [config 與 certificate 設定參考](https://cadlab.mde.tw/post/jupyterhub-oauth2-deng-ru-she-ding.html)
  
  - 預設使用 oauth 驗證，需要申請 certificate：
    
    - 使用 Email 新增使用者會遇到下方訊息，[解決方式參考](https://professorkazarinoff.github.io/jupyterhub-engr114/google_oauth/)


    > Please enter a username matching the regular expression configured via the NAME_REGEX

    > 要加入 c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']

  - 若有使用 `docker-compose down` 再重新啟動後使用者資料都會重置， `config_folder` 資料夾內的資料也是方便未來移植、複製使用者資料
    
## Build image and start containers
  
  ```
  docker-compose up -d
  ```
  - Build images：第一次啟動/或改動 `dockerfile` 
  
  ```
  docker-compose up --build -d
  ```
  - 手動重啟
  
  ```
  docker-compose restart
  ```

## Stops containers

  ```
  docker-compose down
  ```

## JupyterHub URL

  依需求更換 port，並確認是否可以連線

  ```
  http://<IP-Adress>:8000
  ```

## 使用 oauth 驗證帳號設定
  
  在 admin 頁面新增即可
  ```
  http://<yourdomain.onead.tw>:8000/hub/admin
  ```

## 非使用 oauth 驗證帳號設定(新增/刪除/修改)

  1.更新

  ```
  sudo docker exec -it jupyterhub passwd <user>
  ```
  2.新增

  ```
  sudo docker exec -it jupyterhub useradd --create-home <user>
  sudo docker exec -it jupyterhub passwd <user>
  ```
  若有新增使用者必須在 admin 頁面也新增一樣名稱的使用者，否則 Jupyter 不會認得
  ```
  http://<IP-Adress>:8000/hub/admin
  ```

  3.刪除

  未確定該使用者的資料都不需要時請勿加上 `-r`

  ```
  sudo docker exec -it jupyterhub userdel <user>
  ```





