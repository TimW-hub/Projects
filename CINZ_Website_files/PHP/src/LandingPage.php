<?php

use Page;
use SilverStripe\Assets\Image;
use SilverStripe\AssetAdmin\Forms\UploadField;

class LandingPage extends Page 
{
	private static $allowed_children = [
		BasicSubpage::class,
		Page::class,
		LandingPage::class,
	];
	
    private static $has_one = [
        'Photo' => Image::class,
	];

	public function getCMSFields() 
	{
		$fields = parent::getCMSFields();
		$fields->addFieldToTab('Root.Images', UploadField::create('Photo'));
		return $fields;
	}
}