FROM php:7.4-apache
WORKDIR /var/www/html
#WORKDIR /project/php
#COPY . .

COPY ./php/index.html /var/www/html/index.html
COPY /private/etc/apache2/httpd.conf /usr/local/apache2/conf/httpd.conf
#COPY /php/index.html /var/www/html

# #FROM php:7.4-apache

# WORKDIR /var/www/html

# # MySQL拡張機能をインストール
# RUN docker-php-ext-install mysqli pdo pdo_mysql

# # ApacheのRewriteモジュールを有効化
# RUN a2enmod rewrite

# # アプリケーションのコードをコピー
# COPY . .

# # Apacheの再起動（設定の反映のため）
# RUN service apache2 restart

# # ポート80を公開
# EXPOSE 80

# # Apacheはデフォルトで起動