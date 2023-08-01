import boto3

S3= boto3.client("s3")

print("::AWS S3 Manager::\n\n")
print("""
    Create Bucket:     <press>1
    List Bucket:       <press>2
    Delete Bucket:     <press>3
    \n
    List Object(files):<press>4
    File Upload:       <press>5
    Download File:     <press>6
    Delete File:       <press>7
      \n
    Get File Metadata: <press>8
    Exit...!           <press>9

""")


while True:
    option= int(input("Enter your Choice:  "))

    if option==1:
        name=input("Enter Bucket Name: ")
        region=input("Enter Region: ")
        S3.create_bucket( Bucket=name,ACL='private',CreateBucketConfiguration={'LocationConstraint': region} )
        print("\nSuccessfully Created:....!")
    
    elif option==2:
        list = S3.list_buckets()
        for bucket in list["Buckets"]:
            print(bucket["Name"])
    
    elif option==3:
        name=input("Enter Bucket Name: ")
        S3.delete_bucket(Bucket=name)
        print("\nSuccessfully Deleted:....!")

    elif option==4:
        name=input("Enter Bucket Name: ")
        files = S3.list_objects(Bucket=name)
        for file in files["Contents"]:
            print(file["Key"])

    elif option==5:
        name=input("Enter Bucket Name: ")
        file=input("Enter File Path: ")
        fileName=input("Enter file Name: ")
        S3.upload_file(Bucket=name,Filename=file,Key=fileName)
        print(f"\nSuccessfully Uploded as a name {fileName}:....!")

    elif option==6:
        name=input("Enter Bucket Name: ")
        fileName=input("Enter file Name: ")
        S3.download_file(Bucket=name,Key=fileName,Filename=fileName)
        print("\nSuccessfully Downloaded:....!")

    elif option==7:
        name=input("Enter Bucket Name: ")
        fileName=input("Enter file Name: ")
        S3.delete_object(Bucket=name,Key=fileName)

    elif option==8:
        name=input("Enter Bucket Name: ")
        fileName=input("Enter file Name: ")
        metadata = S3.head_object(Bucket=name,Key=fileName)
        print("Metadata of File:......!\n")
        print(metadata)

    elif option==9:
        break

