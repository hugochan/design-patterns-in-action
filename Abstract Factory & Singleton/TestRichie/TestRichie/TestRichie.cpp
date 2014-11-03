// TestRichie.cpp : Defines the entry point for the console application.
//

#include "TestRichie.h"
#include <iostream>
#include <stddef.h>

using namespace std;


#define TestRichie
#define TestAdvancedRichie
#define TestSuperRichie
#define TestUltraRichie

Richie* Richie::instance = NULL;
AdvancedRichie* AdvancedRichie::instance = NULL;
SuperRichie* SuperRichie::instance = NULL;
UltraRichie* UltraRichie::instance = NULL;


int main(int argc, char**argv)
{
	cout << "======================================" << endl;
	cout << "------------Test Richie---------------" << endl;
	cout << "-------------------------by Yu Chen---" << endl;

	cout << "======================================" << endl;

#ifdef TestRichie
	Richie* richie = (Richie*)AbstractRichie::GetConcreteRichie(RICHIE);
	Richie* r = (Richie*)AbstractRichie::GetConcreteRichie(RICHIE);
	if (richie == r) cout << "Richie has already been instantiated!" << endl;
	// test
	richie->TestCPU();
	richie->TestMMU();
	richie->TestMotherboard();
	delete richie;
#endif

#ifdef TestAdvancedRichie
	AdvancedRichie* advanced_richie = (AdvancedRichie*)AbstractRichie::GetConcreteRichie(ADVANCEDRICHIE);
	AdvancedRichie* r1 = (AdvancedRichie*)AbstractRichie::GetConcreteRichie(ADVANCEDRICHIE);
	if (advanced_richie == r1) cout << "Advanced Richie has already been instantiated!" << endl;
	// test
	advanced_richie->TestCPU();
	advanced_richie->TestMMU();
	advanced_richie->TestMotherboard();
	delete advanced_richie;
#endif

#ifdef TestSuperRichie
	SuperRichie* super_richie = (SuperRichie*)AbstractRichie::GetConcreteRichie(SUPERRICHIE);
	SuperRichie* r2 = (SuperRichie*)SuperRichie::GetConcreteRichie(ADVANCEDRICHIE);
	if (super_richie == r2) cout << "Super Richie has already been instantiated!" << endl;
	// test
	super_richie->TestCPU();
	super_richie->TestMMU();
	super_richie->TestMotherboard();
	delete super_richie;
#endif

#ifdef TestUltraRichie
	UltraRichie* ultra_richie = (UltraRichie*)AbstractRichie::GetConcreteRichie(ULTRARICHIE);
	UltraRichie* r3 = (UltraRichie*)UltraRichie::GetConcreteRichie(ADVANCEDRICHIE);
	if (ultra_richie == r3) cout << "Ultra Richie has already been instantiated!" << endl;
	// test
	ultra_richie->TestCPU();
	ultra_richie->TestMMU();
	ultra_richie->TestMotherboard();
	delete ultra_richie;
#endif
	system("pause");
	return 0;
}

AbstractRichie* AbstractRichie::GetConcreteRichie(int richie_type)
{
	switch (richie_type) {
	case RICHIE:
		return Richie::getInstance();
		break;
	case ADVANCEDRICHIE:
		return AdvancedRichie::getInstance();
		break;
	case SUPERRICHIE:
		return SuperRichie::getInstance();
		break;
	case ULTRARICHIE:
		return UltraRichie::getInstance();
		break;
	default:
		break;
	}

}


void Richie::TestCPU(void)
{
	CPUOfRichie cup_richie;
	cup_richie.test();
}

void Richie::TestMMU(void)
{
	MMUOfRichie mmu_richie;
	mmu_richie.test();
}
void Richie::TestMotherboard(void)
{
	MotherboardOfRichie motherboard_richie;
	motherboard_richie.test();
}

Richie* Richie::getInstance()
{
	if (instance == NULL)
		instance = new Richie;
	return instance;
}

void AdvancedRichie::TestCPU(void)
{
	CPUOfAdvancedRichie cup_advancedrichie;
	cup_advancedrichie.test();
}

void AdvancedRichie::TestMMU(void)
{
	MMUOfAdvancedRichie mmu_advancedrichie;
	mmu_advancedrichie.test();
}
void AdvancedRichie::TestMotherboard(void)
{
	MotherboardOfAdvancedRichie motherboard_advancedrichie;
	motherboard_advancedrichie.test();
}


AdvancedRichie* AdvancedRichie::getInstance()
{
	if (instance == NULL)
		instance = new AdvancedRichie;
	return instance;
}


void SuperRichie::TestCPU(void)
{
	CPUOfSuperRichie cup_superrichie;
	cup_superrichie.test();
}

void SuperRichie::TestMMU(void)
{
	MMUOfSuperRichie mmu_superrichie;
	mmu_superrichie.test();
}
void SuperRichie::TestMotherboard(void)
{
	MotherboardOfSuperRichie motherboard_superrichie;
	motherboard_superrichie.test();
}

SuperRichie* SuperRichie::getInstance()
{
	if (instance == NULL)
		instance = new SuperRichie;
	return instance;
}

void UltraRichie::TestCPU(void)
{
	CPUOfUltraRichie cup_ultrarichie;
	cup_ultrarichie.test();
}

void UltraRichie::TestMMU(void)
{
	MMUOfUltraRichie mmu_ultrarichie;
	mmu_ultrarichie.test();
}
void UltraRichie::TestMotherboard(void)
{
	MotherboardOfUltraRichie motherboard_ultrarichie;
	motherboard_ultrarichie.test();
}


UltraRichie* UltraRichie::getInstance()
{
	if (instance == NULL)
		instance = new UltraRichie;
	return instance;
}

void CPUOfRichie::test(void)
{
	cout << "Richie CPU" << endl;
}

void MMUOfRichie::test(void)
{
	cout << "Richie MMU" << endl;
}

void MotherboardOfRichie::test(void)
{
	cout << "Richie Motherboard" << endl;
}

void CPUOfAdvancedRichie::test(void)
{
	cout << "Advanced Richie CPU" << endl;
}

void MMUOfAdvancedRichie::test(void)
{
	cout << "Advanced Richie MMU" << endl;
}

void MotherboardOfAdvancedRichie::test(void)
{
	cout << "Advanced Richie Motherboard" << endl;
}

void CPUOfSuperRichie::test(void)
{
	cout << "Super Richie CPU" << endl;
}

void MMUOfSuperRichie::test(void)
{
	cout << "Super Richie MMU" << endl;
}

void MotherboardOfSuperRichie::test(void)
{
	cout << "Super Richie Motherboard" << endl;
}

void CPUOfUltraRichie::test(void)
{
	cout << "Ultra Richie CPU" << endl;
}

void MMUOfUltraRichie::test(void)
{
	cout << "Ultra Richie MMU" << endl;
}

void MotherboardOfUltraRichie::test(void)
{
	cout << "Ultra Richie Motherboard" << endl;
}
