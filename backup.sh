#!/bin/bash
TIME=$(date +"%Y-%m-%d_%H-%M")
tar -czf "backup_$TIME.tar.gz" work.txt
echo "--- สำรองข้อมูลเสร็จแล้ว: backup_$TIME.tar.gz ---"
