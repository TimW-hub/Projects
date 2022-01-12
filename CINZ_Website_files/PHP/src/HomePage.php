<?php

use Page;
use SilverStripe\Versioned\Versioned;
use SilverStripe\Forms\FieldList;
use SilverStripe\Forms\GridField\GridField;
use SilverStripe\Forms\GridField\GridFieldConfig_RecordEditor;
use SilverStripe\ORM\DataObject;
use SilverStripe\Assets\Image;
use SilverStripe\Forms\TextareaField;
use SilverStripe\Forms\TextField;
use SilverStripe\AssetAdmin\Forms\UploadField;

class HomePage extends Page 
{

	private static $db = [
		'HeaderText' => 'Varchar',
	];

    private static $has_many = [
        'PromoSections' => PromoFields::class,
    ];

    private static $owns = [
        'PromoSections',
    ];
	
	public function getCMSFields() 
	{
		$fields = parent::getCMSFields();
		$fields->removeByName('Content');
		$fields->addFieldToTab('Root.Main', TextareaField::create('HeaderText','Promo Header Text')
		->setDescription('This is the text that appears on the home page main screen image.'), 'Metadata');
		
		$fields->addFieldToTab('Root.PromoSections', GridField::create(
			'PromoSections',
			'Promo Sections',
			$this->PromoSections(),
			GridFieldConfig_RecordEditor::create()
		));
		
		return $fields;
	}
	
}