#!/bin/bash

sudo sh -c 'cat > /etc/nginx/sites-available/myapp << EOF
server {
    listen 80;
    listen [::]:80;
    server_name thich2hand.com; # replace with your domain name

    # # SSL/TLS settings
    # ssl_certificate /path/to/ssl/cert;
    # ssl_certificate_key /path/to/ssl/key;
    # ssl_protocols TLSv1.2 TLSv1.3;
    # ssl_ciphers HIGH:!aNULL:!MD5;

    # Security headers
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options nosniff;
    add_header Referrer-Policy "strict-origin-when-cross-origin";

    location / {
        # Route traffic to product backend server for thich2hand.com
        proxy_pass http://0.0.0.0:81;

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
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/

# Test Nginx configuration file
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
