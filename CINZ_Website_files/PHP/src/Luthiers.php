<?php

use SilverStripe\ORM\DataObject;
use SilverStripe\Forms\FieldList;
use SilverStripe\Forms\TextField;
use SilverStripe\Forms\TextareaField;
use SilverStripe\Forms\CheckboxField;
use SilverStripe\AssetAdmin\Forms\UploadField;
use SilverStripe\ORM\ArrayLib;
use SilverStripe\Assets\Image;
use SilverStripe\Forms\TabSet;

class Luthiers extends DataObject
{
	
	private static $db = [
		'Name' => 'Varchar',
		'Description' => 'Varchar',
	];

	private static $has_one = [
		'Photo' => Image::class,
	];
	
	private static $owns = [
		'Photo',
	];
	
	private static $summary_fields = [
        'Name' => 'Luthier Name',
        'Description' => 'Luthier Description',
		'Photo.Filename' => 'Image file name',
    ];
	
	public function getCMSFields()
	{
		$fields = FieldList::create(TabSet::create('Root'));
		$fields->addFieldsToTab('Root.Main', [
            TextField::create('Name', 'Luthier Name'),
            TextareaField::create('Description', 'Luthier brief description'),
            $uploader = UploadField::create('Photo'),
        ]);
		
		$uploader->setFolderName('luthier-photos');
        $uploader->getValidator()->setAllowedExtensions(['png','gif','jpeg','jpg']);
		
		return $fields;
	}
	
}