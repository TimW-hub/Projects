<?php

use Page;
use SilverStripe\Assets\Image;
use SilverStripe\AssetAdmin\Forms\UploadField;

class BasicSubpage extends Page 
{
	private static $can_be_root = false;
	
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