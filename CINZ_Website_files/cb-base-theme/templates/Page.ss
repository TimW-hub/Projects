<!DOCTYPE html>
<html lang="$ContentLocale">
<head>
    <meta charset="utf-8">
    <% base_tag %>
    <title>$SiteConfig.Title | <% if $MetaTitle %>$MetaTitle<% else %>$Title<% end_if %></title>
    <meta http-equiv="cleartype" content="on">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    $MetaTags(false)

    <!-- Always force latest IE rendering engine -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <% require themedCSS('normalize') %>
    <% require themedCSS('core') %>
    <% require themedCSS('typography') %>
    <% require themedCSS('layout') %>
    <% require themedCSS('form') %>
    <% require themedCSS('print') %>
	<% require themedCSS('homepage') %>
    <% require themedCSS('subpage') %>
    <% require themedCSS('landingpage') %>
    <% require themedCSS('blog') %>

    <%-- Fonts --%>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

    <%-- JavaScript --%>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body class="$ClassName.ShortName">
    <% include Header %>
	<% include SecondaryNav %>
    <% include Navigation %>
    <main>
        $Layout
    </main>

    <% include Footer %>

    <script src="{$ThemeDir}/javascript/script.js"></script>
</body>
</html>