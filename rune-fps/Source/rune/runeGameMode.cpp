// Copyright Epic Games, Inc. All Rights Reserved.

#include "runeGameMode.h"
#include "runeHUD.h"
#include "runeCharacter.h"
#include "UObject/ConstructorHelpers.h"

AruneGameMode::AruneGameMode()
	: Super()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnClassFinder(TEXT("/Game/FirstPersonCPP/Blueprints/FirstPersonCharacter"));
	DefaultPawnClass = PlayerPawnClassFinder.Class;

	// use our custom HUD class
	HUDClass = AruneHUD::StaticClass();
}
