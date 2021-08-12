FROM nginx:1.20.1  AS production-stage

# contentsを配置するディレクトリを作成する
#COPY /myjlab_summer_2021_teamM/frontend/dist /var/work
RUN mkdir -p /var/log/nginx/log\
    && mkdir /var/www\
    && mkdir /var/www/contents
    
COPY docker/frontend/nginx.conf /etc/nginx/conf.d/nginx.conf
COPY docker/frontend/keys/server.crt /etc/nginx/server.crt
COPY docker/frontend/keys/server.key /etc/nginx/server.key
# ビルド環境で構築されたdistディレクトリをnignxの該当のディレクトリに配置する
#COPY /myjlab_summer_2021_teamM/frontend/dist /var/www/contents
RUN chmod 755 -R /var
RUN chmod 400 /etc/nginx/server.key
# nginx.confファイルを配置する
WORKDIR /var/work
# RUN rm -f /etc/nginx/conf.d/*.conf\
#     && rm -f /etc/nginx/nginx.conf\
#     && cp -i *.conf /etc/nginx

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
#CMD ["nginx", "-g", "daemon off;"]