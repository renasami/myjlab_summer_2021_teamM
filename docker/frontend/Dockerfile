FROM node:14.16.0-stretch-slim AS build-stage

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN yarn global add @vue/cli @vue/cli-init

WORKDIR /myjlab_summer_2021_teamM


# FROM nginx:1.20.1  AS production-stage

# # contentsを配置するディレクトリを作成する
# COPY frontend/vue /var/work
# RUN mkdir -p /var/log/nginx/log\
#     && mkdir /var/www\
#     && mkdir /var/www/contents
    
# COPY frontend/nginx.conf /etc/nginx/conf.d/nginx.conf
# COPY frontend/keys/server.crt /etc/nginx/server.crt
# COPY frontend/keys/server.key /etc/nginx/server.key
# # ビルド環境で構築されたdistディレクトリをnignxの該当のディレクトリに配置する
# COPY --from=build-stage /frontend/dist /var/www/contents

# # nginx.confファイルを配置する
# WORKDIR /var/work
# RUN rm -f /etc/nginx/conf.d/*.conf\
#     && rm -f /etc/nginx/nginx.conf\
#     && cp -i *.conf /etc/nginx

# EXPOSE 80 443
# CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
