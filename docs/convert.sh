#!/usr/bin/env bash

branch="$(git branch --show-current)"
default="master"
echo "current branch: ${branch}"

if [[ "${1}" == "branch" ]]; then
	if [[ "${branch}" != "${default}" ]]; then
		echo "patching tutorials..."
		sed -ri "s@(quick_install.sh) +(-[^b])@\1 -b ${branch} \2@g;s@(V-pipe)/${default}(/utils)@\1/${branch}\2@g" ./*.md
		## example command to keep the output with errors
		# jupytext --to ipynb --pipe-fmt ipynb --pipe 'jupyter nbconvert --to ipynb --execute --allow-errors --stdin --stdout' ./*.md
	else
		echo -e "\e[32;1mNo need to patch branch.\e[0m The default branch is already \`${branch}\`"
	fi
elif [[ "${branch}" != "${default}" ]]; then
	echo -e "\e[33;1mWarning: installer in tutorials will still clone the \`${default}\` branch!\e[0m Use \`$0 branch\` to patch them on the fly and instll the current branch \`${branch}\`"
fi

# create Jupyter Notebooks for all Markdown files
exec jupytext --set-formats ipynb,md --execute ./*.md
