[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12;
(new-object net.webclient).DownloadFile('https://github.com/01org/mkl-dnn/releases/download/v0.12/mklml_win_2018.0.1.20171227.zip', 'mkl.zip')
Expand-Archive 'mkl.zip' 'mkl'
$Extracted_Mkl=(Get-ChildItem 'mkl').FullName
ForEach ($Item in Get-ChildItem ($Extracted_Mkl)){
    Copy-Item $Item.Fullname -destination 'mkl' -Recurse
}
Remove-Item $Extracted_Mkl -Force -Recurse 
Remove-Item 'mkl.zip' -Force -Recurse