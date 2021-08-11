FROM node:14.16.0-stretch-slim

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN yarn global add @vue/cli @vue/cli-init

WORKDIR /myjlab_summer_2021_teamM


FROM nginx:1.20.1  as production-stage

# contentsを配置するディレクトリを作成する
COPY nginx/work/ /home/work
RUN mkdir -p /var/log/nginx/log\
    && mkdir /home/www\
    && mkdir /home/www/contents

# ビルド環境で構築されたdistディレクトリをnignxの該当のディレクトリに配置する
COPY --from=build-stage /app/dist /home/www/contents

# nginx.confファイルを配置する
WORKDIR /home/work
RUN rm -f /etc/nginx/conf.d/*.conf\
    && rm -f /etc/nginx/nginx.conf\
    && cp -i *.conf /etc/nginx

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;","-c","/etc/nginx/nginx.conf"]
