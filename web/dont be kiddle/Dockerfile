FROM php:7.4-fpm

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git unzip nginx

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www/html/
RUN git clone https://github.com/laravel/laravel.git

WORKDIR /var/www/html/laravel/
RUN git checkout .
RUN composer install
RUN composer require facade/ignition==2.5.1
RUN cp .env.example .env
RUN php artisan key:generate
RUN chgrp -R www-data storage
RUN chmod -R ug+rwx storage
RUN echo 'MTACTF{this_is_not_real_flag}' > /secret.flag

WORKDIR /etc/nginx/sites-available/
RUN sed -i 's/listen = 9000/listen = \/var\/run\/php-fpm.sock/' /usr/local/etc/php-fpm.d/zz-docker.conf
RUN echo 'listen.owner = www-data' >> /usr/local/etc/php-fpm.d/zz-docker.conf
RUN echo 'listen.group = www-data' >> /usr/local/etc/php-fpm.d/zz-docker.conf
RUN echo 'listen.mode = 0660' >> /usr/local/etc/php-fpm.d/zz-docker.conf
RUN echo 'disable_functions = _getppid, allow_url_fopen, allow_url_include, chgrp, chmod, chown, curl_exec, curl_multi_exec, diskfreespace, dl, exec, fpaththru, getmypid, getmyuid, highlight_file, ignore_user_abord, lchgrp, lchown, leak, link, listen, parse_ini_file, passthru, pcntl_exec, popen, posix, posix_ctermid, posix_getcwd, posix_getegid, posix_geteuid, posix_getgid, posix_getgrgid, posix_getgrnam, posix_getgroups, posix_getlogin, posix_getpgid, posix_getpgrp, posix_getpid, posix_getpwnam, posix_getpwuid, posix_getrlimit, posix_getsid, posix_getuid, posix_isatty, posix_kill, posix_mkfifo, posix_setegid, posix_seteuid, posix_setgid, posix_setpgid, posix_setsid, posix_setuid, posix_times, posix_ttyname, posix_uname, proc_close, proc_get_status, proc_nice, proc_open, proc_terminate, putenv, set_time_limit, shell_exec, show_source, source, system, virtual, assert, mail' >> /usr/local/etc/php/conf.d/docker-php-ext-sodium.ini
RUN echo 'server {\n\tlisten 80;\n\tlisten [::]:80;\n\n\troot /var/www/html/laravel/public;\n\n\tadd_header X-Frame-Options "SAMEORIGIN";\n\tadd_header X-Content-Type-Options "nosniff";\n\n\tindex index.php;\n\n\tcharset utf-8;\n\n\tlocation / {\n\t\ttry_files $uri $uri/ /index.php?$query_string;\n\t}\n\n\tlocation = /favicon.ico { access_log off; log_not_found off; }\n\tlocation = /robots.txt  { access_log off; log_not_found off; }\n\n\terror_page 404 /index.php;\n\n\tlocation ~ \.php$ {\n\t\tfastcgi_pass unix:/var/run/php-fpm.sock;\n\t\tfastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;\n\t\tinclude fastcgi_params;\n\t}\n\n\tlocation ~ /\.(?!well-known).* {\n\t\tdeny all;\n\t}\n}' > default

RUN echo '#!/bin/bash\nservice nginx restart\nphp-fpm' > /opt/cmd.sh
RUN chmod +x /opt/cmd.sh

CMD ["/opt/cmd.sh"]