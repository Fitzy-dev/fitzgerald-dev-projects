# Jordan Fitzgerald
# 4/24/2026
# RISC-V Processor Simulator

registers = [0] * 32 # 32 registers, initialized to 0
memory = {} # Memory is a dictionary mapping addresses to values
pc = 0 # Program counter

# Give some reisters starting values for testing
registers[1] = 10
registers[2] = 5
registers[9] = 0

# Helper functions
def hex_to_binary(hex_instruction):
    return format(int(hex_instruction, 16), "032b")

# Function to sign-extend a value based on the number of bits
def sign_extend(value, bits):
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value

# Function to get register name from number
def get_register_name(reg_num):
    return f"x{reg_num}"

# Function to print the current state of registers
def print_registers():
    print("\nRegisters:")
    for i in range(32):
        print(f"x{i}: {registers[i]}")
    print()

# Decode the instruction and extract fields
def decode_instruction(hex_instruction):
    binary = hex_to_binary(hex_instruction)
    instruction = int(hex_instruction, 16)

    opcode = instruction & 0x7F
    rd = (instruction >> 7) & 0x1F
    funct3 = (instruction >> 12) & 0x7
    rs1 = (instruction >> 15) & 0x1F
    rs2 = (instruction >> 20) & 0x1F
    funct7 = (instruction >> 25) & 0x7F

    print("\nHex Instruction:", hex_instruction)
    print("Binary:", binary)
    print("Opcode:", format(opcode, "07b"))
    print("rd:", get_register_name(rd))
    print("rs1:", get_register_name(rs1))
    print("rs2:", get_register_name(rs2))
    print("funct3:", format(funct3, "03b"))
    print("funct7:", format(funct7, "07b"))

    return instruction, opcode, rd, funct3, rs1, rs2, funct7

# Execute the instruction based on the opcode and funct3/funct7 fields
def execute_instruction(hex_instruction):
    global pc

    instruction, opcode, rd, funct3, rs1, rs2, funct7 = decode_instruction(hex_instruction)

    # R-Type: add, sub, and, or, xor
    if opcode == 0b0110011:
        if funct3 == 0b000 and funct7 == 0b0000000:
            registers[rd] = registers[rs1] + registers[rs2]
            print(f"\nInstruction: add x{rd}, x{rs1}, x{rs2}")

        elif funct3 == 0b000 and funct7 == 0b0100000:
            registers[rd] = registers[rs1] - registers[rs2]
            print(f"\nInstruction: sub x{rd}, x{rs1}, x{rs2}")

        elif funct3 == 0b111:
            registers[rd] = registers[rs1] & registers[rs2]
            print(f"\nInstruction: and x{rd}, x{rs1}, x{rs2}")

        elif funct3 == 0b110:
            registers[rd] = registers[rs1] | registers[rs2]
            print(f"\nInstruction: or x{rd}, x{rs1}, x{rs2}")

        elif funct3 == 0b100:
            registers[rd] = registers[rs1] ^ registers[rs2]
            print(f"\nInstruction: xor x{rd}, x{rs1}, x{rs2}")

        else:
            print("\nUnknown R-Type instruction")

        pc += 4

    # I-Type: addi, ld
    elif opcode == 0b0010011:
        imm = (instruction >> 20) & 0xFFF
        imm = sign_extend(imm, 12)

        if funct3 == 0b000:
            registers[rd] = registers[rs1] + imm
            print(f"\nInstruction: addi x{rd}, x{rs1}, {imm}")
        else:
            print("\nUnknown I-Type instruction")

        pc += 4

    elif opcode == 0b0000011:
        imm = (instruction >> 20) & 0xFFF
        imm = sign_extend(imm, 12)

        address = registers[rs1] + imm

        if funct3 == 0b011:
            registers[rd] = memory.get(address, 0)
            print(f"\nInstruction: ld x{rd}, {imm}(x{rs1})")
        else:
            print("\nUnknown load instruction")

        pc += 4

    # S-Type: sd
    elif opcode == 0b0100011:
        imm_11_5 = (instruction >> 25) & 0x7F
        imm_4_0 = (instruction >> 7) & 0x1F
        imm = (imm_11_5 << 5) | imm_4_0
        imm = sign_extend(imm, 12)

        address = registers[rs1] + imm

        if funct3 == 0b011:
            memory[address] = registers[rs2]
            print(f"\nInstruction: sd x{rs2}, {imm}(x{rs1})")
        else:
            print("\nUnknown store instruction")

        pc += 4

    # B-Type: beq, bne
    elif opcode == 0b1100011:
        imm_12 = (instruction >> 31) & 0x1
        imm_10_5 = (instruction >> 25) & 0x3F
        imm_4_1 = (instruction >> 8) & 0xF
        imm_11 = (instruction >> 7) & 0x1

        imm = (imm_12 << 12) | (imm_11 << 11) | (imm_10_5 << 5) | (imm_4_1 << 1)
        imm = sign_extend(imm, 13)

        if funct3 == 0b000:
            print(f"\nInstruction: beq x{rs1}, x{rs2}, {imm}")
            if registers[rs1] == registers[rs2]:
                pc += imm
            else:
                pc += 4

        elif funct3 == 0b001:
            print(f"\nInstruction: bne x{rs1}, x{rs2}, {imm}")
            if registers[rs1] != registers[rs2]:
                pc += imm
            else:
                pc += 4

        else:
            print("\nUnknown branch instruction")
            pc += 4

    else:
        print("\nUnknown opcode")
        pc += 4

    registers[0] = 0
    print("PC:", pc)
    print_registers()


def main():
    print("RISC-V Processor Simulator")
    print("Supported instructions: and, or, xor, add, sub, addi, ld, sd, beq, bne")
    print("Enter 'quit' to stop.\n")

    while True:
        hex_instruction = input("Enter hex instruction: ").strip()

        if hex_instruction.lower() == "quit":
            print("Program ended.")
            break

        try:
            execute_instruction(hex_instruction)
        except ValueError:
            print("Invalid hex instruction. Try again.")


if __name__ == "__main__":
    main()
