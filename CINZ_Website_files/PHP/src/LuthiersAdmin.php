<?php

use SilverStripe\Admin\ModelAdmin;

class LuthiersAdmin extends ModelAdmin
{

    private static $menu_title = 'Luthiers';

    private static $url_segment = 'luthiers';

    private static $managed_models = [
		Luthiers::class,
    ];
	
	private static $menu_icon_class = 'font-icon-torso';
	
	private static $menu_priority = 7;
}