# Use a minimal, production-ready Nginx image
FROM nginx:stable-alpine

# Remove default content and use a custom Nginx configuration
RUN rm -rf /usr/share/nginx/html/*

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html

# Expose standard HTTP port
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
