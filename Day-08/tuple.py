gcs_bucket_list = ("mani_demo_bucket", "abhi_demo_bucket", "john_demo_bucket", "pavan_demo_bucket")

print(gcs_bucket_list)

print(len(gcs_bucket_list))

print(gcs_bucket_list[0])

print(gcs_bucket_list[0] + "  " + gcs_bucket_list[3])

new_list = gcs_bucket_list[0:2]
print(new_list)
print(len(new_list))