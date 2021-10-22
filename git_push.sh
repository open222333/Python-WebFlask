time=$(date "+%Y%m%d-%H%M%S")
read -p "commit title:" title
read -p "commit description:" commit_d
commit_d="${time} - ${title}"
git add *
git commit -m "${commit_t}" -m "${commit_d}"
git push origin main