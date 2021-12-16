# USE Alpine as base image
FROM alpine:3.13

# Install required utilities
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --no-cache bash chromium fluxbox novnc supervisor websockify x11vnc xvfb

# Copy configuration files
RUN ln -s /usr/share/novnc/vnc_lite.html /usr/share/novnc/index.html
COPY supervisord.conf /etc/supervisord.conf
COPY menu /root/.fluxbox/menu
COPY entry.sh /entry.sh

# Environment variables
ENV DISPLAY :0
ENV RESOLUTION=1024x768
ENV PYTHONPATH=/usr/lib/python3.9/site-packages/

# Expose ports
EXPOSE 6901 5901

RUN chmod +x /entry.sh

# Entry point
CMD ["/bin/bash", "-c", "/entry.sh"]
