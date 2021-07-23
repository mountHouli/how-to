# Python + Poetry + Lambda

Lambda operates based on `requirements.txt`, not your Poetry virtual env.

Also, remember you have to `sam build`.



## Error 1

Given: Your `pyenv` global python version is different than the python version in your `template.yaml`.

`sam build` will fail.

Fix:
`pyenv local 3.8.6`



## Error 2

Requirements (i.e requirements.txt) file not found.

Install requests into your Poetry virtual env:
`poetry add requests`

`poetry export --without-hashes -f requirements.txt -o requirements.txt --with-credentials`



## SAM only needs the requirements.txt file

...not any of the package code.

It SAM/CF uses the requirements.txt file to download the packages from somewhere.



## Make

https://www.gnu.org/software/make/



## Miscellaneous

### python3.8 dotenv problem

- https://stackoverflow.com/questions/59572174/no-module-named-dotenv-python-3-8/67813391#67813391
