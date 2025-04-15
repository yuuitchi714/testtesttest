FROM php:7.4-apache
WORKDIR /var/www/html
#WORKDIR /project/php
#COPY . .

COPY ./php/index.html /var/www/html/index.html
COPY ./php/index.php /var/www/html/inddex.php
COPY ./php/apache2/mods-enabled/ /var/www/html/apache2/mods-enabled/
COPY ./php/apache2/mods-available/dir.conf /var/www/html/apache2/mods-available/dir.conf
COPY ./php/apache2/apache2.conf /var/www/html/apache2/apache2.conf
#COPY /Users/ichi/path/to/your/project/php/apache2/httpd.conf /etc/apache2/apache2.conf
#COPY ./php /var/www/html
#llllllggggjjg
# #FROM php:7.4-apache

#WORKDIR /var/www/html

# # MySQL拡張機能をインストール
# RUN docker-php-ext-install mysqli pdo pdo_mysql

# # ApacheのRewriteモジュールを有効化
RUN a2enmod dir

# # アプリケーションのコードをコピー
# COPY . .

# # Apacheの再起動（設定の反映のため）
RUN service apache2 restart

# # ポート80を公開
#EXPOSE 80

# # Apacheはデフォルトで起動