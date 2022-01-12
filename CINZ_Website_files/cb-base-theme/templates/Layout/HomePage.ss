<div class="homepage-main">
    <% loop $PromoSections %>
    <div class="homepage-loop">
        <div class="info-blog $EvenOdd">
            <h2>$HomeTitle</h2>
            <p>$HomeBlurb</p>
        </div>
		<div class="image image-large">
            $Photo.Fill(720,720)
        </div>
		<a href="#" class="$EvenOdd">
            <span class="readmore-btn">Read More >></span>
        </a>
    </div>
    <% end_loop %>
</div>