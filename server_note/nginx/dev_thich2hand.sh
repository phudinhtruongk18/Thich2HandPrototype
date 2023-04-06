#!/bin/bash

sudo sh -c 'cat > /etc/nginx/sites-available/dev.thich2hand << EOF
server {
    listen 80;
    listen [::]:80;
    server_name dev.thich2hand.com; # replace with your domain name

    # Security headers
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options nosniff;
    add_header Referrer-Policy "strict-origin-when-cross-origin";

    location / {
        # Route traffic to product backend server for thich2hand.com
        proxy_pass http://0.0.0.0:82;

        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;

    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        internal;
    }

}
EOF'

# Create symbolic link to Nginx configuration file
sudo ln -s /etc/nginx/sites-available/dev.thich2hand /etc/nginx/sites-enabled/

# Test Nginx configuration file
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
