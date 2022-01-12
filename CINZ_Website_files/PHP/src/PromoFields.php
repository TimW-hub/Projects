<?php

use SilverStripe\Versioned\Versioned;
use SilverStripe\Forms\FieldList;
use SilverStripe\Forms\GridField\GridField;
use SilverStripe\Forms\GridField\GridFieldConfig_RecordEditor;
use SilverStripe\ORM\DataObject;
use SilverStripe\Assets\Image;
use SilverStripe\Forms\TextareaField;
use SilverStripe\Forms\TextField;
use SilverStripe\AssetAdmin\Forms\UploadField;

class PromoFields extends DataObject
{

	private static $db = [
		'HomeTitle' => 'Varchar',
		'HomeBlurb' => 'Varchar',
	];

	private static $has_one = [
		'Photo' => Image::class,
		'HomePage' => HomePage::class,
	];
	
	private static $extensions = [
		Versioned::class,
	];
	
	private static $versioned_gridfield_extensions = true;
	
	private static $owns = [
		'Photo',
	];
	
	private static $summary_fields = [
        'HomeTitle' => 'Title',
        'HomeBlurb' => 'Section Text',
		'Photo.Filename' => 'Photo file name',
    ];
	
	public function getCMSFields()
	{
		$fields = FieldList::create(
            TextField::create('HomeTitle', 'Title'),
            TextareaField::create('HomeBlurb', 'Short info section'),
            $uploader = UploadField::create('Photo')
        );
		
		$uploader->setFolderName('homepage-photos');
        $uploader->getValidator()->setAllowedExtensions(['png','gif','jpeg','jpg']);
		
		return $fields;
	}
}