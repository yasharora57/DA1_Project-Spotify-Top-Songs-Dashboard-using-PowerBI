# Spotify Top Songs Dashboard

![Spotify Dashboard](
https://github.com/yasharora57/DA1_Project-Spotify-Top-Songs-Dashboard-using-PowerBI/blob/31c9327e87eff6d154ab7d3e56b9faffa6922a24/db_picture.png
)

This repository contains a Power BI dashboard that provides an in-depth analysis of the top Spotify songs for 2023. The dashboard includes various visualizations and insights derived from the dataset, which can be downloaded from Kaggle. Below is a guide on how to set up and use the dashboard.

## Dataset

The dataset used for this dashboard can be downloaded from Kaggle:
- [Top Spotify Songs 2023 Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download)

The dataset includes the following information:
- Track name
- Artist(s) name
- Release date
- Spotify playlists and charts
- Streaming statistics
- Various audio features

## Dashboard Features

The Power BI dashboard provides the following analysis and visualizations:

1. **Album Cover Images**: 
   - Use the Spotify Developer API to generate client ID and secret.
   - Use the provided Python script to attach cover image URLs to the dataset.
   - Add a custom visual in Power BI named HTML Content to embed album cover images dynamically.

2. **Energy Level % per Song**:
   - Add a custom DENEB visual and embed the provided Vega-Deneb gauge code to show energy levels.

3. **Number of Songs Released per Day**:
   - Use a custom Heatmap visual to depict the number of songs released each day of a particular month.

4. **Overall Analysis**:
   - Average streams per year (KPI card)
   - Top song streams vs. average streams in % difference (KPI card)
   - Tracks by release date (line chart)
   - Track by streams (bar chart)
   - Track Stats and Music infos are shown in multi KPI cards)
   - Date, track and artist are used as slicer filters.

## How to Use

1. **Download the Power BI Dashboard**:
   - Download the attached Power BI dashboard file from this repository.

2. **Change the Data Source**:
   - Open the Power BI file.
   - Go to `Home` > `Transform Data` > `Data Source Settings`.
   - Change the data source to the location of your downloaded dataset.

3. **Explore the Dashboard**:
   - Use the slicers (Date, Track, Artist) to filter the data.
   - Explore the various visualizations and insights provided by the dashboard.

## Additional Resources

- [Vega-Deneb Gauge Code](https://stackoverflow.com/questions/75881301/convert-vega-deneb-gauge-to-work-in-powerbi)
- [Deneb Heatmap Template](https://github.com/PowerBI-tips/Deneb-Templates/blob/main/templates/heatmap%20with%20bars%20-%20red%20themed.json)
