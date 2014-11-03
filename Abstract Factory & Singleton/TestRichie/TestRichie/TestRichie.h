// TestRichie.h : Declare the class for the console application.
//

// abstract factory
class AbstractRichie
{
public:
	#define RICHIE 0
    #define ADVANCEDRICHIE 1
	#define SUPERRICHIE 2
	#define ULTRARICHIE 3

	void TestCPU(void);
	void TestMMU(void);
	void TestMotherboard(void);
	static AbstractRichie* GetConcreteRichie(int richie_type);
protected:
	//AbstractRichie();
};

// concrete factory
// Richie
class Richie : public AbstractRichie
{
public:
	void TestCPU(void);
	void TestMMU(void);
	void TestMotherboard(void);
	static Richie* getInstance(void);
private:
	static Richie* instance;
	Richie(){};
};

// Advanced Richie
class AdvancedRichie : public AbstractRichie
{
public:
	void TestCPU(void);
	void TestMMU(void);
	void TestMotherboard(void);
	static AdvancedRichie* getInstance(void);

private:
	static AdvancedRichie* instance;
	AdvancedRichie(){};
};

// Super Richie
class SuperRichie : public AbstractRichie
{
public:
	void TestCPU(void);
	void TestMMU(void);
	void TestMotherboard(void);
	static SuperRichie* getInstance(void);

private:
	static SuperRichie* instance;
	SuperRichie(){};
};

// Ultra Richie
class UltraRichie : public AbstractRichie
{
public:
	void TestCPU(void);
	void TestMMU(void);
	void TestMotherboard(void);
	static UltraRichie* getInstance(void);

private:
	static UltraRichie* instance;
	UltraRichie(){};
};

// abstract product
// CPU
class CPU
{
public:
	void test(void);
private:

};

// MMU
class MMU
{
public:
	void test(void);
private:

};

// Motherboard
class Motherboard
{
public:
	void test(void);
private:

};

// concrete product
// CPUOfRichie
class CPUOfRichie : public CPU
{
public:
	void test(void);
private:

};

// CPUOfAdvancedRichie
class CPUOfAdvancedRichie : public CPU
{
public:
	void test(void);
private:

};

// CPUOfSuperRichie
class CPUOfSuperRichie : public CPU
{
public:
	void test(void);
private:

};

// CPUOfUltraRichie
class CPUOfUltraRichie : public CPU
{
public:
	void test(void);
private:

};

// MMUOfRichie
class MMUOfRichie : public MMU
{
public:
	void test(void);
private:

};

// MMUOfAdvancedRichie
class MMUOfAdvancedRichie : public MMU
{
public:
	void test(void);
private:

};

// MMUOfSuperRichie
class MMUOfSuperRichie : public MMU
{
public:
	void test(void);
private:

};

// MMUOfUltraRichie
class MMUOfUltraRichie : public MMU
{
public:
	void test(void);
private:

};

// MotherboardOfRichie
class MotherboardOfRichie : public Motherboard
{
public:
	void test(void);
private:

};

// MotherboardOfAdvancedRichie
class MotherboardOfAdvancedRichie : public Motherboard
{
public:
	void test(void);
private:

};

// MotherboardOfSuperRichie
class MotherboardOfSuperRichie : public Motherboard
{
public:
	void test(void);
private:

};

// MotherboardOfUltraRichie
class MotherboardOfUltraRichie : public Motherboard
{
public:
	void test(void);
private:

};
