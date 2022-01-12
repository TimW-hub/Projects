<h1>$Title</h1>
$Content
$Form

<div id="lp-preview-grid">
<% loop $Children %>
    <a href="$Link">
    <div class="subpage-preview">
        <img src="$Photo.Link">
        <h2>$Title</h2>
    </div>
    </a>
<% end_loop %>
</div>