from trustpilotreviews import GetReviews
import pandas as pd
# Initiate it. Language will be required
t = GetReviews()

# Pass in web-page address as it appears in trustpilot.com
mate_id = t.get_id('rockar.com')

# Check if everything is ok
if mate_id.ok:
    print(mate_id.business_id)

# Gather data from that id
data = t.get_reviews()
df = pd.DataFrame(t.dictData)
print(df)
df.to_csv(r'C:\Users\SahalNurain\Documents\sentiment analysis\RockarReviews')