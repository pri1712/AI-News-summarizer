# Project Documentation

## Task List
### 1. Get Articles
- [x] Get the articles in XML format from all the RSS feeds and store them in the `all_articles` matrix.
- [ ] Get articles in JSON format from NewsAPI.

### 2. Summarize Articles
- [x] Summarize each article using BART.
- [x] Score summaries and given summaries using BERT, keeping similarity scores ≥ 0.8.
- [ ] Use AI-generated summaries in the PostgreSQL DB.

#### Challenges & Notes:
- [x] Summaries and descriptions from all the RSS feeds are often identical. Need to extract the actual description for summarization.
- [ ] The summaries are not great for short news or recurring content. Explore ways to improve the summaries.
- [x] NYT articles don't provide proper descriptions.
- [ ] Image descriptions are appearing in summaries. Needs filtering.
- [ ] BBC summaries include page descriptions (e.g., ads). Needs cleanup.
- [x] Guardian articles work fine.

### 3. Generate Tags
- [ ] Generate or fetch category tags for each article.

### 4. Database Integration
- [ ] Store articles and summaries in PostgreSQL for ordered collection.
